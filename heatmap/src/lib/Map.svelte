<script>
  /* Data points defined as an array of LatLng objects */
  import { Loader } from "google-maps";
  import { onMount } from "svelte";
  import axios from "axios";

  const options = {
    libraries: ["visualization"],
  };
  const loader = new Loader("AIzaSyC4b08DEC4qqEXGfdc1dKNi2dQKvv1cB4U", options);

  onMount(async () => {
    try {
      const res = await axios.get(
        // This URL has to be adjusted when backend runs in production. so far using localhost ngrok
        "https://91df-192-41-114-224.eu.ngrok.io/get-coordinates"
      );
      console.log(res);
      if (res.data) {
        const coordinates = res.data.coordinates;
        loadTheMap(coordinates);
      }
    } catch (err) {
      console.log(err);
      console.log("Coordinates failed to load");
    }
  });

  const loadTheMap = async (data) => {
    loader.load().then(function (google) {
      var heatmapData = data.map((coor) => {
        const date = new Date(coor["time-stamp"] * 1000);
        console.log(date);
        return {
          location: new google.maps.LatLng(coor.latitude, coor.longitude),
          weight: 5,
        };
      });
      console.log("Loaded");

      var sanFrancisco = new google.maps.LatLng(29.439325, 106.887703);

      const map = new google.maps.Map(document.getElementById("map"), {
        center: sanFrancisco,
        zoom: 6,
        mapTypeId: "satellite",
      });

      var heatmap = new google.maps.visualization.HeatmapLayer({
        data: heatmapData,
      });
      heatmap.set("radius", 30);
      heatmap.setMap(map);
    });
  };
</script>

<div id="map" />

<style>
  #map {
    width: 100vw;
    /* min-width: 1000px; */
    height: 100vh;
    position: absolute;
    top: 0;
    left: 0;
    z-index: 1;
  }
</style>
