<?php

namespace App\Http\Controllers;

use Log;
use Illuminate\Http\Request;
use Jenkinsmgmt\Helpers\Helper;
use Validator;
use App\Resultado;

class ResultadoController extends Controller {

  public function getAllResultado(Request $request, $id) {
    $resultados=Resultado::where('competicionID', '=', $id)->get();
    return response()->json($resultados);
  }
  public function getXornada(Request $request, $c, $x) {
    $resultados=Resultado::where('competicionID', '=', $c)
                          ->where('Xornada', '=', $x)
                          ->get();
    return response()->json($resultados);
  }
  public function getResultadoByID(Request $request, $id) {
    $resultados=Resultado::find($id);
    return response()->json($resultados);
  }
  public function getNumeroXornadas(Request $request, $c) {
    $resultados=Resultado::where('competicionID', '=', $c)
                          ->groupby('Xornada')
                          ->select('Xornada')
                          ->get();
    return response()->json($resultados);
  }
}
