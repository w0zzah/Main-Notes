let activePanel = null;

const panels = document.querySelectorAll(".panel");
const homeButton = document.getElementById("homeButton");

panels.forEach(panel => {
    const title = panel.querySelector(".panel-title");

    title.addEventListener("click", () => openPanel(panel));
});

function openPanel(panel) {

    if (activePanel === panel) return;

    closeAllPanels();

    panel.classList.add("active");
    activePanel = panel;

    panels.forEach(p => {
        if (p !== panel) {
            p.classList.add("fade");
        }
    });

    homeButton.classList.add("visible");
}

function closeAllPanels() {
    panels.forEach(p => {
        p.classList.remove("active");
        p.classList.remove("fade");
    });

    activePanel = null;
    homeButton.classList.remove("visible");
}

homeButton.addEventListener("click", closeAllPanels);



