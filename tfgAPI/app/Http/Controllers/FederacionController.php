<?php

namespace App\Http\Controllers;

use Log;
use Illuminate\Http\Request;
use Jenkinsmgmt\Helpers\Helper;
use Validator;
use App\Deporte;
use App\Federacion;


class FederacionController extends Controller {

  public function getAllFederacion() {
    $federacion=Federacion::join('Deporte', 'Deporte.ID', '=', 'Federacion.deporteID')
                            ->select('Federacion.Nome as Nome', 'Federacion.ID as Federacion_ID', 'Deporte.Nome as Deporte')
                            ->get();
    return response()->json($federacion);
  }

  public function getFederacionByDeporte(Request $request, $id)  {
    $rules =  array(
      'id'    => 'required'
    );

    $messages = array(
      'id.required' => 'id is required.'
    );
    $validator = \Validator::make(array('id' => $id), $rules, $messages);

    if(!$validator->fails()) {
      $federacion=Federacion::join('Deporte', 'Deporte.ID', '=', 'Federacion.deporteID')
                              ->select('Federacion.Nome as Nome', 'Federacion.ID as Federacion_ID', 'Deporte.Nome as Deporte')
                              ->where('deporteID','=',$id)
                              ->get();
      return response()->json($federacion);
    } else {
      $errors = $validator->errors();
      return response()->json($errors->all());
    }
  }

  public function getFederacionByID(Request $request, $id)  {
    $rules =  array(
      'id'    => 'required'
    );

    $messages = array(
      'id.required' => 'id is required.'
    );
    $validator = \Validator::make(array('id' => $id), $rules, $messages);

    if(!$validator->fails()) {
      $federacion=Federacion::join('Deporte', 'Deporte.ID', '=', 'Federacion.deporteID')
                              ->select('Federacion.Nome as Nome', 'Federacion.ID as Federacion_ID', 'Deporte.Nome as Deporte')
                              ->where('Federacion.ID','=',$id)
                              ->get();
      return response()->json($federacion);
    } else {
      $errors = $validator->errors();
      return response()->json($errors->all());
    }
  }
}
