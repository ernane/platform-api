<?php

require __DIR__ . '/vendor/autoload.php';

$app = new Slim\App;

$app->get('/', function ($request, $response) {
    return '<h1>Hello World. Slim<h1>';
});

$app->run();
