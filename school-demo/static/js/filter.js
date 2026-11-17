// Client-side search and filter for lists of cards or news items.
// Markup contract:
//   [data-filter-root]    wrapper that contains the controls and items
//   [data-filter-search]  text input, matched against each item's text
//   [data-filter-select]  dropdown, matched against data-filter-value
//   [data-filter-item]    one item, with an optional data-filter-value
//   [data-filter-count]   optional element that shows "X of Y"
//   [data-filter-empty]   optional message shown when nothing matches
(function () {
  const roots = document.querySelectorAll("[data-filter-root]");

  roots.forEach(function (root) {
    const items = Array.from(root.querySelectorAll("[data-filter-item]"));
    const search = root.querySelector("[data-filter-search]");
    const select = root.querySelector("[data-filter-select]");
    const count = root.querySelector("[data-filter-count]");
    const empty = root.querySelector("[data-filter-empty]");

    function applyFilters() {
      const query = search ? search.value.trim().toLowerCase() : "";
      const value = select ? select.value : "";
      let shown = 0;

      items.forEach(function (item) {
        const matchesText = !query || item.textContent.toLowerCase().indexOf(query) !== -1;
        const matchesValue = !value || item.dataset.filterValue === value;
        const visible = matchesText && matchesValue;
        item.hidden = !visible;
        if (visible) shown += 1;
      });

      if (count) {
        count.textContent = "Showing " + shown + " of " + items.length;
      }
      if (empty) {
        empty.hidden = shown !== 0;
      }
    }

    if (search) search.addEventListener("input", applyFilters);
    if (select) select.addEventListener("change", applyFilters);

    applyFilters();
  });
})();
