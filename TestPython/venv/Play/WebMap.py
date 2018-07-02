import folium

map = folium.Map(location=[32.014253, 34.787647]  , tiles="Mapbox Bright")  #Creatig a map object
map.add_child(folium.Marker(location=[32.014253, 34.787647],popup="Hi I am Marker" ,icon=folium.Icon(color='green')))    #Adding a marker


#Exmaple 2
fg = folium.FeatureGroup(name = "My Map")
fg.add_child(folium.Marker(location=[32.014253, 34.787647],popup="Hi I am Marker" ,icon=folium.Icon(color='green')))
map.add_child(fg)

#Exmaple 3 - Multiple markers
fg = folium.FeatureGroup(name = "My Map")
fg.add_child(folium.Marker(location=[32.014253, 34.787647],popup="Hi I am Marker" ,icon=folium.Icon(color='green')))
fg.add_child(folium.Marker(location=[32.3, 34.8],popup="Hi I am Marker" ,icon=folium.Icon(color='blue')))
map.add_child(fg)


#or
fg = folium.FeatureGroup(name = "My Map")
for coor in [[32.014253, 34.787647] ,[32.3, 34.8]]:
    fg.add_child(folium.Marker(location=coor,popup="Hi I am Marker" ,icon=folium.Icon(color='green')))


#Map with marker form a file
map = folium.Map(location=[32.014253, 34.787647]  , tiles="Mapbox Bright")  #Creatig a map object
map.add_child(folium.Marker(location=[32.3, 34.8] ,popup="Hi I am Marker" ,icon=folium.Icon(color='blue')))
map.add_child(fg)
map.save("C:/Users/yarona/Downloads/Map.html")   #Created a Map Html File

