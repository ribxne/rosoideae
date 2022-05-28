<script>
  export let colors = ["#ffffff"];

  function addColor() {
    colors.push("#000000");
    colors = colors;

    console.log(colors);
  }
</script>

<div class="container">
  {#each colors as color}
    <input type="color" bind:value={color} />
  {/each}

  <button on:click={addColor} class="add">+</button>
</div>

<style>
  .add {
    background-color: transparent;
    height: 5rem;
    width: 5rem;
    border: solid;
    border-width: 5px;
    border-color: #5f6b9d;
    color: #5f6b9d;
    font-size: 3rem;
    padding: 0;
    margin-top: 0;
  }

  .container {
    display: flex;
    flex-direction: row;
    align-items: stretch;
    gap: 0.5rem;
  }
</style>
