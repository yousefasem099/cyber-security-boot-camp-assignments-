
<?php

// 1. Set JSON response header
header("Content-Type: application/json; charset=UTF-8");

// 2. Get HTTP request method
$method = $_SERVER['REQUEST_METHOD'];

// 3. Get request headers
$headers = function_exists('getallheaders')
    ? getallheaders()
    : [];

// 4. Read request body
$input = file_get_contents("php://input");

// 5. Decode JSON data
$data = json_decode($input, true);

// 6. Validate JSON format
if ($input !== '' && json_last_error() !== JSON_ERROR_NONE) {

    http_response_code(400);

    echo json_encode([
        "status" => "error",
        "message" => "Invalid JSON format",
        "error" => json_last_error_msg()
    ], JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);

    exit;
}

// 7. Process HTTP methods
switch ($method) {

    case "GET":

        http_response_code(200);

        $response = [
            "status" => "success",
            "method" => "GET",
            "message" => "Data retrieved successfully",
            "headers" => $headers
        ];

        break;

    case "POST":

        http_response_code(201);

        $response = [
            "status" => "success",
            "method" => "POST",
            "message" => "Data created successfully",
            "received_data" => $data
        ];

        break;

    case "PUT":

        http_response_code(200);

        $response = [
            "status" => "success",
            "method" => "PUT",
            "message" => "Data updated successfully",
            "received_data" => $data
        ];

        break;

    case "DELETE":

        http_response_code(200);

        $response = [
            "status" => "success",
            "method" => "DELETE",
            "message" => "Data deleted successfully"
        ];

        break;

    default:

        http_response_code(405);

        $response = [
            "status" => "error",
            "method" => $method,
            "message" => "Method Not Allowed"
        ];

        break;
}

// 8. Return JSON response
echo json_encode(
    $response,
    JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE
);

?>
