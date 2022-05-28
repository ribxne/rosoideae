<script>
  import { setBrightness } from "./request.js";
</script>

<h1>Set brightness</h1>
<input
  type="range"
  min="0"
  max="1"
  step="0.1"
  on:change={(e) => setBrightness(e.target.value)}
/>
<h3>
  or just
  <button class="off" on:click={() => setBrightness(0)}
    ><strong>turn it off</strong></button
  >
</h3>

<style>
  .off {
    background-color: #af364f;
    color: #ffffff;
  }
</style>
