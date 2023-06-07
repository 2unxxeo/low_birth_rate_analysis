import geopandas as gpd
import folium
import pandas as pd
from pyproj import CRS, Transformer

seoul_geo = gpd.read_file('seoul_geo.json', encoding='utf8')

def wgs84_to_utm_crs(lat, lon):
    utm_zone_number = int((lon + 180) / 6) + 1
    utm_zone = f"{utm_zone_number if lat >= 0 else -utm_zone_number}"
    utm_crs = CRS.from_proj4(f"+proj=utm +zone={utm_zone} +ellps=WGS84 +datum=WGS84 +units=m +_defs")
    return utm_crs

map_seoul = folium.Map(location=[37.5665, 126.9780], zoom_start=12, font_path='C:/Windows/Fonts/nanum.ttf')

birthrate_data = pd.read_csv('구별_합계출산율.csv')
marriage_rate_data = pd.read_csv('구별_조혼인율.csv')
income_data = pd.read_csv('구별_2021_1인당_근로소득.csv')

birthrate_heatmap = folium.Choropleth(
    geo_data=seoul_geo,
    name='출산율',
    data=birthrate_data,
    key_on='feature.properties.name',
    columns=['구이름', '2021'],
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='출산율',
    show=True,
).add_to(map_seoul)

marriage_rate_heatmap = folium.Choropleth(
    geo_data=seoul_geo,
    name='혼인율',
    data=marriage_rate_data,
    key_on='feature.properties.name',
    columns=['구이름', '2021'],
    fill_color='PuBuGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='혼인율',
    show=False,
).add_to(map_seoul)

income_layer = folium.Choropleth(
    geo_data=seoul_geo,
    name='소득',
    data=income_data,
    key_on='feature.properties.name',
    columns=['구이름', '2021'],
    fill_color='GnBu',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='1인당 근로소득',
    show=False,
).add_to(map_seoul)

def folium_del_legend(choropleth):
    choropleth.geojson.add_child(folium.features.GeoJsonTooltip(fields=[], labels=False))
    for key in choropleth._children:
        if key.startswith('color_map'):
            del choropleth._children[key]
    return choropleth

birthrate_heatmap = folium_del_legend(birthrate_heatmap)
marriage_rate_heatmap = folium_del_legend(marriage_rate_heatmap)
income_layer = folium_del_legend(income_layer)

for idx, row in birthrate_data.iterrows():
    district = row['구이름']
    birthrate = row['2021']
    marriage_rate = marriage_rate_data.loc[marriage_rate_data['구이름'] == district, '2021'].values[0]
    income = income_data.loc[income_data['구이름'] == district, '2021'].values[0]

    district_boundary = seoul_geo[seoul_geo['name'] == district]

    utm_crs = wgs84_to_utm_crs(37.5665, 126.9780)  # 서울의 위도, 경도
    district_boundary_utm = district_boundary.to_crs(utm_crs)
    district_centroid_utm = district_boundary_utm.centroid
    district_centroid = district_centroid_utm.to_crs("EPSG:4326")
    popup_location = (district_centroid.y.values[0], district_centroid.x.values[0])

    folium.Marker(
        location=popup_location,
        icon=folium.DivIcon(
            html=f'<div style="writing-mode: vertical-lr; font-weight: bold; font-size: 20px; text-align: center;">{district}</div>'
        ),
        popup=folium.Popup(f'{district}: 출산율 {birthrate}%, 혼인율 {marriage_rate}%, 1인당 근로소득 {income}', max_width=300, max_height=200),
    ).add_to(map_seoul)

top_income_districts = income_data.nlargest(3, '2021')
bottom_income_districts = income_data.nsmallest(3, '2021')

income_layer_group = folium.FeatureGroup(name='소득 최상/최하 3구')

for idx, row in top_income_districts.iterrows():
    district = row['구이름']
    district_boundary = seoul_geo[seoul_geo['name'] == district]
    folium.GeoJson(
        district_boundary,
        name=f'소득 최상 3구: {district}',
        style_function=lambda x: {'fillColor': 'green', 'color': 'green', 'weight': 2, 'fillOpacity': 0.3}
    ).add_to(income_layer_group)

for idx, row in bottom_income_districts.iterrows():
    district = row['구이름']
    district_boundary = seoul_geo[seoul_geo['name'] == district]
    folium.GeoJson(
        district_boundary,
        name=f'소득 최하 3구: {district}',
        style_function=lambda x: {'fillColor': 'red', 'color': 'red', 'weight': 2, 'fillOpacity': 0.3}
    ).add_to(income_layer_group)

income_layer_group.add_to(map_seoul)

layer_control = folium.LayerControl(position='topright', collapsed=False, autoZIndex=False, hideSingleBase=True)
map_seoul.add_child(layer_control)
map_seoul.save('seoul_map.html')
