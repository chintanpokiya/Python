import java.util.HashMap;
import java.util.InputMismatchException;
import java.util.Map;
import java.util.Scanner;

public class WatchStoreManagement
{
    private static Map<String, String> users = new HashMap<>();
    private static Map<Integer, Watch> inventory = new HashMap<>();
    private static Map<String, Integer> cart = new HashMap<>();
    private static String currentUser = "";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String role;

        do {
            role = mainMenu(scanner);

            if (role.equals("admin")) {
                adminLogin(scanner);
                if (!currentUser.isEmpty()) {
                    adminMenu(scanner);
                }
            } else if (role.equals("user")) {
                userLogin(scanner);
                if (!currentUser.isEmpty()) {
                    userMenu(scanner);
                }
            } else if (role.equals("admin_register")) {
                adminRegister(scanner);
            } else if (role.equals("user_register")) {
                userRegister(scanner);
            } else {
                System.out.println("Invalid choice. Please try again.");
            }
        } while (!role.isEmpty());

        scanner.close();
    }

    private static String mainMenu(Scanner scanner) {
        System.out.println("Welcome to the Watch Store Management System");
        System.out.println("1. Admin Register");
        System.out.println("2. User Register");
        System.out.println("3. Admin Login");
        System.out.println("4. User Login");
        System.out.println("0. Exit");
        System.out.print("Select an option: ");
        int choice = readInteger(scanner);

        switch (choice) {
            case 1:
                return "admin_register";
            case 2:
                return "user_register";
            case 3:
                return "admin";
            case 4:
                return "user";
            case 0:
                return "";
            default:
                return "";
        }
    }

    private static void adminRegister(Scanner scanner) {
        try {
            System.out.print("Enter new admin username: ");
            String username = scanner.nextLine();

            if (users.containsKey(username)) {
                System.out.println("Username already exists. Please choose another one.");
                return;
            }

            System.out.print("Enter new admin password: ");
            String password = scanner.nextLine();
            users.put(username, password);
            System.out.println("Admin registration successful.");
        } catch (Exception e) {
            System.out.println("An error occurred: " + e.getMessage());
        }
    }

    private static void userRegister(Scanner scanner) {
        try {
            System.out.print("Enter new user username: ");
            String username = scanner.nextLine();

            if (users.containsKey(username)) {
                System.out.println("Username already exists. Please choose another one.");
                return;
            }

            System.out.print("Enter new user password: ");
            String password = scanner.nextLine();
            users.put(username, password);
            System.out.println("User registration successful.");
        } catch (Exception e) {
            System.out.println("An error occurred: " + e.getMessage());
        }
    }

    private static void adminLogin(Scanner scanner) {
        System.out.print("Enter admin username: ");
        String username = scanner.nextLine();
        System.out.print("Enter admin password: ");
        String password = scanner.nextLine();

        if (!users.containsKey(username) || !users.get(username).equals(password)) {
            System.out.println("Invalid admin username or password.");
            return;
        }

        currentUser = username;
        System.out.println("Admin login successful.");
    }

    private static void userLogin(Scanner scanner) {
        System.out.print("Enter user username: ");
        String username = scanner.nextLine();
        System.out.print("Enter user password: ");
        String password = scanner.nextLine();

        if (!users.containsKey(username) || !users.get(username).equals(password)) {
            System.out.println("Invalid user username or password.");
            return;
        }

        currentUser = username;
        System.out.println("User login successful.");
    }

    private static void adminMenu(Scanner scanner) {
        int choice;

        do {
            System.out.println("\nAdmin Menu:");
            System.out.println("1. Add Watch");
            System.out.println("2. Update Watch Price");
            System.out.println("3. Delete Watch");
            System.out.println("4. View All Watches");
            System.out.println("0. Logout");
            System.out.print("Enter your choice: ");
            choice = readInteger(scanner);

            switch (choice) {
                case 1:
                    addWatch(scanner);
                    break;
                case 2:
                    updateWatchPrice(scanner);
                    break;
                case 3:
                    deleteWatch(scanner);
                    break;
                case 4:
                    viewAllWatches();
                    break;
                case 0:
                    System.out.println("Logging out...");
                    currentUser = "";
                    break;
                default:
                    System.out.println("Invalid choice. Please enter a number between 0 and 4.");
                    break;
            }
        } while (choice != 0);
    }

    private static void userMenu(Scanner scanner) {
        int choice;

        do {
            System.out.println("\nUser Menu:");
            System.out.println("1. View All Watches");
            System.out.println("2. Add Watch to Cart");
            System.out.println("3. View Cart");
            System.out.println("0. Logout");
            System.out.print("Enter your choice: ");
            choice = readInteger(scanner);

            switch (choice) {
                case 1:
                    viewAllWatches();
                    break;
                case 2:
                    addWatchToCart(scanner);
                    break;
                case 3:
                    viewCart();
                    break;
                case 0:
                    System.out.println("Logging out...");
                    currentUser = "";
                    break;
                default:
                    System.out.println("Invalid choice. Please enter a number between 0 and 3.");
                    break;
            }
        } while (choice != 0);
    }

    private static void addWatch(Scanner scanner) {
        System.out.print("Enter watch name: ");
        String name = scanner.nextLine();
        System.out.print("Enter watch quantity: ");
        int quantity = readInteger(scanner);
        System.out.print("Enter watch price: ");
        double price = scanner.nextDouble();
        scanner.nextLine(); // Consume newline

        int id = inventory.size() + 1;
        inventory.put(id, new Watch(id, name, quantity, price));

        System.out.println("Watch added successfully.");
    }

    private static void updateWatchPrice(Scanner scanner) {
        System.out.print("Enter watch ID: ");
        int id = readInteger(scanner);

        if (inventory.containsKey(id)) {
            System.out.print("Enter new price: ");
            double price = scanner.nextDouble();
            inventory.get(id).setPrice(price);
            System.out.println("Price updated successfully.");
        } else {
            System.out.println("Watch not found.");
        }
    }

    private static void deleteWatch(Scanner scanner) {
        System.out.print("Enter watch ID: ");
        int id = readInteger(scanner);

        if (inventory.containsKey(id)) {
            inventory.remove(id);
            System.out.println("Watch deleted successfully.");
        } else {
            System.out.println("Watch not found.");
        }
    }

    private static void viewAllWatches() {
        System.out.println("\nAll Watches:");
        System.out.println("ID\tName\tQuantity\tPrice");
        for (Watch watch : inventory.values()) {
            System.out.println(watch.getId() + "\t" + watch.getName() + "\t" + watch.getQuantity() + "\t\t" + watch.getPrice());
        }
    }

    private static void addWatchToCart(Scanner scanner) {
        System.out.print("Enter watch ID to add to cart: ");
        int id = readInteger(scanner);

        if (inventory.containsKey(id)) {
            if (cart.containsKey(currentUser)) {
                cart.put(currentUser, cart.get(currentUser) + 1);
            } else {
                cart.put(currentUser, 1);
            }
            System.out.println("Watch added to cart successfully.");
        } else {
            System.out.println("Watch not found.");
        }
    }

    private static void viewCart() {
        if (cart.containsKey(currentUser)) {
            System.out.println("\nYour Cart:");
            System.out.println("Watch ID\tQuantity");
            System.out.println(currentUser + "'s Cart:");
            System.out.println(currentUser + "\t" + cart.get(currentUser));
        } else {
            System.out.println("Your cart is empty.");
        }
    }

    private static int readInteger(Scanner scanner) {
        int input = -1;
        try {
            input = scanner.nextInt();
            scanner.nextLine(); // Consume newline
        } catch (InputMismatchException e) {
            System.out.println("Invalid input. Please enter a number.");
            scanner.nextLine(); // Consume invalid input
        }
        return input;
    }

    private static class Watch {
        private int id;
        private String name;
        private int quantity;
        private double price;

        public Watch(int id, String name, int quantity, double price) {
            this.id = id;
            this.name = name;
            this.quantity = quantity;
            this.price = price;
        }

        public int getId() {
            return id;
        }

        public String getName() {
            return name;
        }

        public int getQuantity() {
            return quantity;
        }

        public void setQuantity(int quantity) {
            this.quantity = quantity;
        }

        public double getPrice() {
            return price;
        }

        public void setPrice(double price) {
            this.price = price;
        }
    }
}
