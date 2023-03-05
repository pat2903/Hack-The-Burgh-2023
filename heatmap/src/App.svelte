<script>
  import svelteLogo from "./assets/svelte.svg";
  import Counter from "./lib/Map.svelte";
  import Map from "./lib/Map.svelte";
</script>

<main id="main">
  <div />
  <h1 id="heading">Tracking vulnerable species</h1>
  <div id="background" />
  <div id="sidebar">
    <h2>Color key</h2>
    <ul>
      <li style="padding: 1rem 0">
        <div style="display:flex; justify-content:space-between">
          Seen in last 7 days <div
            class="color-box"
            style="background-color: red"
          />
        </div>
      </li>
      <li style="padding: 1rem 0">
        <div style="display:flex; justify-content:space-between">
          Seen in last 30 days <div
            class="color-box"
            style="background-color: orange"
          />
        </div>
      </li>
      <li style="padding: 1rem 0">
        <div style="display:flex; justify-content:space-between">
          Seen in last 6 months  <div
            class="color-box"
            style="background-color: yellow"
          />
        </div>
      </li>
      <li style="padding: 1rem 0">
        <div style="display:flex; justify-content:space-between">
          Seen in last 2 years <div
            class="color-box"
            style="background-color: green"
          />
        </div>
      </li>
    </ul>
  </div>
  <Map />
</main>

<style>
  #main {
    width: 100%;
    height: 100%;
    position: relative;
  }
  #background {
    background: linear-gradient(to bottom, rgb(0, 0, 0, 0.7), rgb(0, 0, 0, 0));
    width: 100vw;
    height: 100vh;
    position: absolute;
    top: 0;
    left: 0;
    z-index: 2;
    pointer-events: none;
  }
  #sidebar {
    top: 5rem;
    left: 2rem;
    background-color: #fff;
    width: 18rem;
    height: 50vh;
    position: absolute;
    z-index: 3;
    padding: 2rem;
  }
  .color-box {
    width: 30px;
    height: 30px;
  }
  #heading {
    position: absolute;
    top: 5vh;
    left: calc(50vw - (/* width */ 420px / 2));
    z-index: 100;
    color: #fff;
  }
</style>
