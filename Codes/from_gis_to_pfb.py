
lombardy_shp_pr = '/home/leonardo/Documents/Codes_git/Water-alliance/Source/GIS/area_lombardia_pr.shp'

rasterized = '/home/leonardo/Documents/Codes_git/Water-alliance/Source/GIS/rasterized.tif'


processing.run("gdal:rasterize", {'INPUT':lombardy_shp_pr,'FIELD':'ID_2','BURN':None,\
    'USE_Z':False,'UNITS':0,'WIDTH':250,'HEIGHT':250,\
        'EXTENT':'8.4994,11.4287,44.6809,46.6381 [EPSG:32632]','NODATA':0,'OPTIONS':''\
            ,'DATA_TYPE':5,'INIT':None,'INVERT':False,'EXTRA':'','OUTPUT':rasterized})

Dummy_Mask = '/home/leonardo/Documents/Codes_git/Water-alliance/Source/GIS/Dummy_Mask.tif'
processing.run("native:fillnodata", {'INPUT':rasterized,'BAND':1,'FILL_VALUE':1,'OUTPUT':Dummy_Mask})

Mask = '/home/leonardo/Documents/Codes_git/Water-alliance/Source/GIS/Mask.tif'
processing.run("native:fillnodata", {'INPUT':rasterized,'BAND':1,'FILL_VALUE':0,'OUTPUT':Mask})




DEM_all_region = QgsRasterLayer('/home/leonardo/Documents/Codes_git/Water-alliance/Source/GIS/elevation.tif')
DEM = '/home/leonardo/Documents/Codes_git/Water-alliance/Source/GIS/DEM.tif'
entries = []

ras = QgsRasterCalculatorEntry()
ras.ref = 'ras@1'
ras.raster = DEM_all_region
ras.bandNumber = 1
entries.append(ras)

calc = QgsRasterCalculator('ras_a@1 +1.0', DEM, 'Gtiff', DEM_all_region.extent(), QgsCoordinateReferenceSystem("EPSG:32632"), DEM_all_region.width(), DEM_all_region.height(), entries)

calc.processCalculation()