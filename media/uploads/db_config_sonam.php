<?php
$host = "localhost";
$username = "sonam";
$password = "";
$database = "cafemanagementsystem";

$conn = new mysqli($host, $username, $password, $database);

if ($conn->connect_error) {
    die("Database connection failed: " . $conn->connect_error);
}
?>
