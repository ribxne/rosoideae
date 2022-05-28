<script>
  import Brightness from "./brightness.svelte";
  import Fill from "./fill.svelte";
  import Pattern from "./pattern.svelte";
  import Gradient from "./gradient.svelte";
  import Tabs from "./Tabs.svelte";

  let items = [
    { label: "Brightness", value: 1, component: Brightness },
    { label: "Fill", value: 2, component: Fill },
    { label: "Pattern", value: 3, component: Pattern },
    { label: "Gradient", value: 4, component: Gradient },
  ];
</script>

<Tabs {items} />
