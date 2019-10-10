package application;

import java.awt.Color;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;

public class MainController {
	@FXML
	private Label stt;
	@FXML
	private TextField user;
	@FXML
	private PasswordField pwd;

	public void btnlogin(ActionEvent event) {
		if (user.getText().matches("admin") && pwd.getText().matches("2018")) {
			stt.setText("Login Success");

		} else {
			stt.setText("Login Failed");
		}
	}
}
