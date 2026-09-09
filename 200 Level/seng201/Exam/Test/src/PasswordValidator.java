import java.util.ArrayList;
import java.util.List;

public class PasswordValidator {

    public void checkPassword(String username, String password) {
        List<String> errors = new ArrayList<>();

        boolean hasUsername = username != null && username.length() > 0;
        if (!hasUsername) {
            errors.add("You need a username");
        }

        if (password == null || password.length() < 12) {
            errors.add("The length of your password must be at least 12");
        }

        if (hasUsername && password != null && password.contains(username)) {
            errors.add("Your username can't be contained in your password");
        }

        if (errors.isEmpty()) {
            System.out.println("The password is OK");
        } else {
            String finalMessage = String.join(" and ", errors);
            finalMessage = finalMessage.substring(0, 1).toUpperCase() + finalMessage.substring(1);
            System.out.println(finalMessage);
        }
    }
}

