<?php

/** @var \Laravel\Lumen\Routing\Router $router */

/*
|--------------------------------------------------------------------------
| Application Routes
|--------------------------------------------------------------------------
|
| Here is where you can register all of the routes for an application.
| It is a breeze. Simply tell Lumen the URIs it should respond to
| and give it the Closure to call when that URI is requested.
|
*/

/*$router->get('/', function () use ($router) {
    return 'Hola Mundo!';
});*/


$router->group([
    'prefix' => 'api/v1',
], function () use ($router){


    //Deporte Controller
    $router->get('/deporte', 'DeporteController@getAllDeporte');
    $router->get('/deporte/{id}', 'DeporteController@getDeporteByID');

       //Federacion controller
    $router->get('/federacion', 'FederacionController@getAllFederacion');
    $router->get('deporte/{id}/federacion', 'FederacionController@getFederacionByDeporte');
    $router->get('federacion/{id}', 'FederacionController@getFederacionByID');


    //Competicion controller
    $router->get('federacion/{id}/competicion', 'CompeticionController@getCompeticionByFederacion');
    $router->get('competicion/{id}', 'CompeticionController@getCompeticionByID');

    //Resultado controller
    $router->get('competicion/{id}/resultado', 'ResultadoController@getAllResultado');
    $router->get('competicion/{c}/resultado/xornada{x}', 'ResultadoController@getXornada');
    $router->get('competicion/{c}/resultado/xornada', 'ResultadoController@getNumeroXornadas');
    $router->get('resultado/{id}', 'ResultadoController@getResultadoByID');
});
