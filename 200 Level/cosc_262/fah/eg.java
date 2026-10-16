package seng201.nunbutblood.gui;

import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.scene.layout.FlowPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;
import seng201.nunbutblood.models.Saints;
import seng201.nunbutblood.models.Covenant;
import seng201.nunbutblood.models.Item;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

/**
 * Controller for the Church Management (hub) screen.
 * Displays the active party, reserves, and inventory. Allows the player to:
 * bench/activate Saints, retire Saints, equip or use items, navigate to
 * the Market, or begin the next Crusade.
 */
public class HubController {

    @FXML private Label covenantTitle;
    @FXML private Label faithLabel;
    @FXML private Label expeditionLabel;
    @FXML private Label partyLabel;
    @FXML private Label statusLabel;

    // Swapped ListViews for Layout Panes to hold our custom UI Cards
    @FXML private FlowPane activePane;
    @FXML private FlowPane reservePane;
    @FXML private VBox inventoryPane;

    private Stage stage;
    private ScreenNavigator navigator;
    private Covenant covenant;

    public void init(Stage stage, ScreenNavigator navigator, Covenant covenant) {
        this.stage = stage;
        this.navigator = navigator;
        this.covenant = covenant;
        refresh();
    }

    /** Refreshes all displayed data from the Covenant model. */
    private void refresh() {
        covenantTitle.setText("⛪  " + covenant.getName().toUpperCase());
        faithLabel.setText("Faith: " + covenant.getFaith());
        expeditionLabel.setText("Crusade " + covenant.getCurrentCrusade()
                + " / " + covenant.getTotalCrusades());
        partyLabel.setText("Party: " + covenant.getActiveParty().size() + "/5");

        refreshActiveParty();
        refreshReserves();
        refreshInventory();
    }

    private void refreshActiveParty() {
        activePane.getChildren().clear();
        for (Saints a : covenant.getActiveParty()) {
            Button benchBtn = new Button("BENCH");
            benchBtn.setOnAction(e -> {
                if (!covenant.benchApostle(a)) {
                    statusLabel.setText("Cannot bench: party must keep at least one Apostle, or reserves are full.");
                } else {
                    statusLabel.setText(a.getName() + " moved to reserves.");
                    refresh();
                }
            });

            Button retireBtn = new Button("RETIRE");
            retireBtn.setOnAction(e -> {
                if (!covenant.retireSaint(a)) {
                    statusLabel.setText("Cannot retire the last Apostle.");
                } else {
                    statusLabel.setText(a.getName() + " has retired.");
                    refresh();
                }
            });

            HBox actions = new HBox(5, benchBtn, retireBtn);
            actions.setAlignment(javafx.geometry.Pos.CENTER);

            VBox card = SaintCardController.createSaintCard(a, actions);
            activePane.getChildren().add(card);
        }
    }

    private void refreshReserves() {
        reservePane.getChildren().clear();
        for (Saints a : covenant.getReserves()) {
            Button activateBtn = new Button("ACTIVATE");
            activateBtn.setOnAction(e -> {
                if (!covenant.activateApostle(a)) {
                    statusLabel.setText("Active party is full (max 5).");
                } else {
                    statusLabel.setText(a.getName() + " added to active party.");
                    a.resetCrusadeCount();
                    refresh();
                }
            });

            Button retireBtn = new Button("RETIRE");
            retireBtn.setOnAction(e -> {
                covenant.retireSaint(a); // No restriction on retiring from reserves
                statusLabel.setText(a.getName() + " has retired.");
                refresh();
            });

            HBox actions = new HBox(5, activateBtn, retireBtn);
            actions.setAlignment(javafx.geometry.Pos.CENTER);

            VBox card = SaintCardController.createSaintCard(a, actions);
            reservePane.getChildren().add(card);
        }
    }

    private void refreshInventory() {
        inventoryPane.getChildren().clear();
        for (Item item : covenant.getInventory()) {
            Button useBtn = new Button("USE / EQUIP");
            useBtn.setOnAction(e -> handleUseItemDialog(item));

            Label itemLabel = new Label(item.getItemName() + " — " + item.getType().name());
            HBox row = new HBox(10, useBtn, itemLabel);
            row.setAlignment(javafx.geometry.Pos.CENTER_LEFT);
            inventoryPane.getChildren().add(row);
        }
    }

    /** Opens a ChoiceDialog allowing the player to select which Apostle to apply the item to. */
    private void handleUseItemDialog(Item item) {
        List<Saints> allSaints = new ArrayList<>(covenant.getActiveParty());
        allSaints.addAll(covenant.getReserves());

        if (allSaints.isEmpty()) {
            statusLabel.setText("You have no Saints to use this on.");
            return;
        }

        ChoiceDialog<Saints> dialog = new ChoiceDialog<>(allSaints.get(0), allSaints);
        dialog.setTitle("Use Item");
        dialog.setHeaderText("Applying: " + item.getItemName());
        dialog.setContentText("Select an Apostle to equip or use this on:");

        Optional<Saints> result = dialog.showAndWait();
        result.ifPresent(apostle -> {
            item.applyEffect(apostle);
            covenant.removeItem(item);
            statusLabel.setText(item.getItemName() + " applied to " + apostle.getName() + "!");
            refresh();
        });
    }

    @FXML
    private void handleMarket() {
        navigator.goToMarket();
    }

    @FXML
    private void handleCrusade() {
        if (covenant.hasLost()) {
            navigator.goToEndScreen(false);
            return;
        }
        if (covenant.isGameComplete()) {
            navigator.goToEndScreen(true);
            return;
        }
        if (covenant.getActiveParty().isEmpty()) {
            statusLabel.setText("You need at least one Apostle in the active party!");
            return;
        }
        navigator.goToCrusadeSelect();
    }
}



    /** Navigates to the Church Management hub using the existing game state. */
    public void goToHub() {
        loadScreen("/fxml/testInterface.fxml", controller -> {
            if (controller instanceof HubController hc) {
                hc.init(stage, this, covenant);
            }
        });
    }


        /**
     * Navigates to the Church Management hub after setup is complete.
     *
     * @param covenant      the newly created Covenant
     * @param marketService the freshly initialised MarketService
     * @param randomSvc     the RandomEventService for this game
     */
    /** Navigates to the Church Management hub using the existing game state. */
    public void goToHub(Covenant covenant, MarketService marketService, RandomService randomSvc) {
        this.covenant = covenant;
        this.marketService = marketService;
        this.randomService = randomSvc;
        goToHub();
    }