package seng201.tut2.gui;

import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.layout.VBox;
import javafx.scene.control.Label;
import javafx.scene.control.Slider;
import javafx.scene.control.TextField;
import seng201.tut2.RocketManager;
import seng201.tut2.models.Rocket;

import java.util.Arrays;
import java.util.List;
import java.util.Objects;
import seng201.tut2.RocketManager;

public class MainScreenController extends ScreenController {

    @FXML private Label Captain;

    @FXML private Label r1NameLabel, r1FuelLabel, r1CleanLabel;
    @FXML private VBox r1Box;

    @FXML private Label r2NameLabel, r2FuelLabel, r2CleanLabel;
    @FXML private VBox r2Box;

    @FXML private Label r3NameLabel, r3FuelLabel, r3CleanLabel;
    @FXML private VBox r3Box;

    public MainScreenController(RocketManager rocketManager) {
        super(rocketManager);
    }

    @Override
    protected String getFxmlFile() {
        return "/fxml/main_screen.fxml";
    }

    @Override
    protected String getTitle() {
        return "";
    }

    @FXML
    public void initialize() {
        String playerName = getRocketManager().getName();
        Captain.setText("Welcome " + playerName + "!");
        refreshUI();
    }

    private void refreshUI() {

        List<Rocket> rockets = getRocketManager().getRocketList();

        // Update the first rocket
        if (!rockets.isEmpty()) {
            updateRocketDisplay(rockets.getFirst(), r1NameLabel, r1FuelLabel, r1CleanLabel);
        }
        if (rockets.size() >= 2) {
            updateRocketDisplay(rockets.get(1), r2NameLabel, r2FuelLabel, r2CleanLabel);
        }
        if (rockets.size() >= 3) {
            updateRocketDisplay(rockets.get(2), r3NameLabel, r3FuelLabel, r3CleanLabel);
        }

    }

    private void updateRocketDisplay(Rocket rocket, Label name, Label fuel, Label cleanliness) {
        name.setText(rocket.getName());
        fuel.setText("Fuel: " + rocket.getFuel());
        cleanliness.setText("Cleanliness: " + rocket.getCleanliness());
    }

    @FXML
    private void onRefuelR1() {
        getRocketManager().getRocketList().get(0).refuel();
        refreshUI();
    }

    @FXML
    private void onCleanR1() {
        getRocketManager().getRocketList().get(0).clean();
        refreshUI();
    }

    @FXML
    private void onRefuelR2() {
        getRocketManager().getRocketList().get(1).refuel();
        refreshUI();
    }

    @FXML
    private void onCleanR2() {
        getRocketManager().getRocketList().get(1).clean();
        refreshUI();
    }
    @FXML
    private void onRefuelR3() {
        getRocketManager().getRocketList().get(2).refuel();
        refreshUI();
    }
    @FXML
    private void onCleanR3() {
        getRocketManager().getRocketList().get(2).clean();
        refreshUI();
    }
}
