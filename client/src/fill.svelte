<script>
  import { setAll } from "./request.js";

  function hexToDec(colorHex) {
    return parseInt(colorHex.substring(1), 16);
  }
</script>

<h1>Click on the square to select a color</h1>
<input type="color" on:change={(e) => setAll(hexToDec(e.target.value))} />
