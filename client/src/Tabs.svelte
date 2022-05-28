<script>
  export let items = [];
  export let activeTabValue = 1;
</script>

<ul>
  {#each items as item}
    <li class={activeTabValue === item.value ? "active" : ""}>
      <span on:click={() => (activeTabValue = item.value)}>{item.label}</span>
    </li>
  {/each}
</ul>
{#each items as item}
  {#if activeTabValue == item.value}
    <div class="box">
      <svelte:component this={item.component} />
    </div>
  {/if}
{/each}

<style>
  .box {
    padding: 3rem;
  }
  ul {
    top: 0;
    left: 0;
    display: flex;
    flex-wrap: wrap;
    padding-left: 0;
    margin-bottom: 0;
    list-style: none;
    background-color: #5f6b9d;
    margin: unset;
  }
  li {
    display: flex;
    font-size: 1.5rem;
  }

  span {
    display: block;
    padding: 0.5rem 1rem;
    cursor: pointer;
  }

  span:hover {
    background-color: #00000080;
  }

  li.active > span {
    background-color: #0d0d0f;
  }
</style>
