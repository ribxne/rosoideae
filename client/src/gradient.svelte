<script>
  import ColorList from "./colorList.svelte";
  import { setGradient } from "./request.js";

  function hexToDec(colorHex) {
    return parseInt(colorHex.substring(1), 16);
  }
</script>

<ColorList />

<button
  class="post"
  type="button"
  on:click={() => setGradient(ColorList.colors.map(hexToDec))}>Apply</button
>
