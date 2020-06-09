library(sp) 
library(ggmap)

gasolineras <- read.csv2('data/preciosEESS_es.csv',header=TRUE,sep=';',stringsAsFactors = FALSE) 
gasolineras <- subset(gasolineras, (!is.na(gasolineras[,7])) & (!is.na(gasolineras[,8]))) 

str(gasolineras)

coordenadas <- gasolineras[,c(7,8)] 
gasolineras_geo <- SpatialPointsDataFrame(coordenadas, gasolineras, proj4string = CRS("+proj=longlat +datum=WGS84 +ellps=WGS84 +towgs84=0,0,0"))

plot(gasolineras_geo)

spain <- get_map(make_bbox(c(-9,3), c(35,45), f=0.05), source="stamen", maptype='watercolor')
ggmap(spain) +
  geom_point(data = gasolineras, aes(x = Longitud, y = Latitud, fill = Precio_gasolina_98), size = 1, shape = 21)
