import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.title("Home")

    st.markdown(
        """
    A [streamlit](https://streamlit.io) app template for geospatial applications based on [streamlit-option-menu](https://github.com/victoryhb/streamlit-option-menu). 
    To create a direct link to a pre-selected menu, add `?page=<app name>` to the URL, e.g., `?page=upload`.
    https://share.streamlit.io/giswqs/streamlit-template?page=upload

    """
    )

    url = "https://github.com/opengeos/datasets/releases/download/raster/wind_global.nc"
    filename = "wind_global.nc"
    leafmap.download_file(url, output=filename, overwrite=True)
    data = leafmap.read_netcdf(filename)
    tif = "wind_global.tif"
    leafmap.netcdf_to_tif(filename, tif, variables=["u_wind", "v_wind"], shift_lon=True)
    geojson = (
    "https://github.com/opengeos/leafmap/raw/master/examples/data/countries.geojson")

    m = leafmap.Map(layers_control=True)
    m.add_raster(tif, indexes=[1], palette="coolwarm", layer_name="u_wind")
    m.add_geojson(geojson, layer_name="Countries")
    m.to_streamlit(height=700)

    m = leafmap.Map(layers_control=True)
    m.add_basemap("CartoDB.DarkMatter")
    m.add_velocity(
        filename,
        zonal_speed="u_wind",
        meridional_speed="v_wind",
        color_scale=[
            "rgb(0,0,150)",
            "rgb(0,150,0)",
            "rgb(255,255,0)",
            "rgb(255,165,0)",
            "rgb(150,0,0)",
        ],
    )
    m.to_streamlit(height=700)

    url = "https://github.com/matheusmgc/streamlit_gee_app/blob/main/Data%20Test%20L3S/L3S_ORBTY_SST_2025_01_29_M3DFS_v1.nc"
    filename = "L3S_ORBTY_SST_2025_01_29_M3DFS_v1.nc"
    leafmap.download_file(url, output=filename, overwrite=True)
    data = leafmap.read_netcdf(filename)
    m = leafmap.Map(layers_control=True)
    #m.add_raster(tif, indexes=[1], palette="coolwarm", layer_name="u_wind")
    m.add_raster(filename, bands=[1], layer_name="teste")
    #m.add_geojson(geojson, layer_name="Countries")
    m.to_streamlit(height=1000)
    #m = leafmap.Map(locate_control=True)
    #m.add_basemap("ROADMAP")
    #m.to_streamlit(height=700)
