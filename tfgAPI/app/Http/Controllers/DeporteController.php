<?php

namespace App\Http\Controllers;

use Log;
use Illuminate\Http\Request;
use Jenkinsmgmt\Helpers\Helper;
use Validator;
use App\Deporte;


class DeporteController extends Controller {

  public function getAllDeporte() {
    $deporte=Deporte::all();
    return response()->json($deporte);
  }

  public function getDeporteByID(Request $request, $id) {
    $deporte=Deporte::find($id);
    return response()->json($deporte);
  }
}
