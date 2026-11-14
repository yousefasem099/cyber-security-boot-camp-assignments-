
<?php
// ==========================================
// SQL Injection Defense - PHP + PDO + SQLite
// ==========================================

// 1. Database connection
try {
    $pdo = new PDO("sqlite::memory:");

    $pdo->setAttribute(
        PDO::ATTR_ERRMODE,
        PDO::ERRMODE_EXCEPTION
    );

    // 2. Create users table
    $pdo->exec("
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            role TEXT NOT NULL
        )
    ");

    // 3. Insert test users
    $users = [
        ['admin', 'admin@example.com', 'Administrator'],
        ['moath', 'moath@example.com', 'User'],
        ['ahmed', 'ahmed@example.com', 'User'],
        ['sara', 'sara@example.com', 'User']
    ];

    $insert = $pdo->prepare("
        INSERT INTO users (username, email, role)
        VALUES (?, ?, ?)
    ");

    foreach ($users as $user) {
        $insert->execute($user);
    }

} catch (PDOException $e) {
    die("Database initialization failed.");
}

// 4. Get user input
$username = $_GET['username'] ?? '';
$mode = $_GET['mode'] ?? 'secure';

$results = [];
$error = '';
$executed = false;

// 5. Execute SQL query
if ($_SERVER['REQUEST_METHOD'] === 'GET'
    && isset($_GET['search'])) {

    $executed = true;

    try {

        if ($mode === 'vulnerable') {

            // INSECURE: Direct input concatenation
            $sql = "SELECT * FROM users
                    WHERE username = '$username'";

            $stmt = $pdo->query($sql);

            $results = $stmt->fetchAll(PDO::FETCH_ASSOC);

        } else {

            // SECURE: Prepared Statement
            $sql = "SELECT * FROM users
                    WHERE username = :username";

            $stmt = $pdo->prepare($sql);

            $stmt->execute([
                ':username' => $username
            ]);

            $results = $stmt->fetchAll(PDO::FETCH_ASSOC);
        }

    } catch (PDOException $e) {

        // Do not expose internal database errors
        $error = "An error occurred while processing your request.";
    }
}

// 6. Output escaping
function clean($value) {
    return htmlspecialchars(
        (string) $value,
        ENT_QUOTES,
        'UTF-8'
    );
}

?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>SQL Injection Defense</title>

    <link rel="stylesheet" href="style.css">
</head>

<body>

<div class="container">

    <header>
        <h1>SQL Injection Defense</h1>
        <p>PHP + PDO + SQLite Security Demonstration</p>
    </header>

    <section class="panel">

        <h2>User Search</h2>

        <form method="GET">

            <label>Username</label>

            <input
                type="text"
                name="username"
                placeholder="Enter username..."
                value="<?= clean($username) ?>"
                required
            >

            <label>Security Mode</label>

            <select name="mode">

                <option value="secure"
                    <?= $mode === 'secure' ? 'selected' : '' ?>>
                    Secure Mode
                </option>

                <option value="vulnerable"
                    <?= $mode === 'vulnerable' ? 'selected' : '' ?>>
                    Vulnerable Mode
                </option>

            </select>

            <button type="submit" name="search">
                Search User
            </button>

        </form>

    </section>

    <?php if ($executed): ?>

        <section class="results">

            <h2>Search Results</h2>

            <?php if ($error): ?>

                <div class="error">
                    <?= clean($error) ?>
                </div>

            <?php elseif (count($results) > 0): ?>

                <div class="success">
                    <?= count($results) ?> record(s) found.
                </div>

                <div class="table-wrapper">

                    <table>

                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>Username</th>
                                <th>Email</th>
                                <th>Role</th>
                            </tr>
                        </thead>

                        <tbody>

                        <?php foreach ($results as $row): ?>

                            <tr>
                                <td><?= clean($row['id']) ?></td>
                                <td><?= clean($row['username']) ?></td>
                                <td><?= clean($row['email']) ?></td>
                                <td><?= clean($row['role']) ?></td>
                            </tr>

                        <?php endforeach; ?>

                        </tbody>

                    </table>

                </div>

            <?php else: ?>

                <div class="warning">
                    No matching users found.
                </div>

            <?php endif; ?>

        </section>

    <?php endif; ?>

    <section class="information">

        <h2>Security Information</h2>

        <?php if ($mode === 'vulnerable'): ?>

            <div class="danger">
                <h3>Vulnerable Mode</h3>
                <p>
                    User input is directly concatenated into SQL.
                    This allows SQL Injection attacks.
                </p>
            </div>

        <?php else: ?>

            <div class="safe">
                <h3>Secure Mode</h3>
                <p>
                    PDO Prepared Statements separate user input
                    from SQL instructions and prevent this
                    form of SQL Injection.
                </p>
            </div>

        <?php endif; ?>

    </section>

    <footer>
        <p>SQL Injection Defense | Cybersecurity Assignment</p>
    </footer>

</div>

</body>
</html>
