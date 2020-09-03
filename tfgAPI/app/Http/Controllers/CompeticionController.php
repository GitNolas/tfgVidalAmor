<?php

namespace App\Http\Controllers;

use Log;
use Illuminate\Http\Request;
use Jenkinsmgmt\Helpers\Helper;
use Validator;
use App\Competicion;
use App\Federacion;


class CompeticionController extends Controller {
  public function getCompeticionByFederacion(Request $request, $id) {
    $resultados=Competicion::where('federacionID', '=', $id)
                          ->get();
    return response()->json($resultados);
  }
  public function getCompeticionByID(Request $request, $id) {
    $resultados=Competicion::find($id);
    return response()->json($resultados);
  }
}
