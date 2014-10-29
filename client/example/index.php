<?php
include_once dirname(__FILE__) . '/../lib/Back.php';
include_once dirname(__FILE__) . '/../lib/Future.php';
include_once dirname(__FILE__) . '/../lib/Client.php';

try {
    $client = new MessagePackRPC_Client('localhost', '18800');
    try {
        $property = $client->call('get_property', array(rand(0, 100)));
        var_dump($property) ;
    } catch (MessagePackRPC_Error_RequestError $e) {
        echo "Error: " . $e->getMessage() . "\n";
    }
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}
