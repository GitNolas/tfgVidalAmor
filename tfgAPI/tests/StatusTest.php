<?php

use Laravel\Lumen\Testing\DatabaseMigrations;
use Laravel\Lumen\Testing\DatabaseTransactions;
use App\Federacion;
use App\Resultado;
use App\Competicion;
class StatusTest extends TestCase
{
    /**
     * Test para a devolucion de todos os deportes da API
     *
     * @return void
     */
    public function testAllDeporte()
    {
      $url="/api/v1/deporte";
      $response = $this->call('GET', $url);
      $this->assertEquals(200, $response->status(), "Erro en {$url}");
    }

    /**
     * Test para a devolucion de todos as federacions por parte da API.
     *
     * @return void
     */
    public function testAllFederacions(){
      $url="/api/v1/federacion";
      $response = $this->call('GET', $url);
      $this->assertEquals(200, $response->status(), "Erro en {$url}");
    }

    /**
     * Test para a chamada a API para devolver as Federacions por ID.
     *
     * @return void
     */
    public function testFederacionsByID(){
      $federacion=Federacion::all();
      foreach($federacion as $f){
        $url="/api/v1/federacion/{$f['ID']}";
        $response = $this->call('GET', $url);
        $this->assertEquals(200, $response->status(), "Erro en {$url}");
      }
    }

    /**
     * Test para a chamada a API para devolver os partidos por ID.
     *
     * @return void
     */
    public function testResultadosByID(){
      $resultado=Resultado::all();
      foreach($resultado as $r){
        $url="/api/v1/resultado/{$r['ID']}";
        $response = $this->call('GET', $url);
        $this->assertEquals(200, $response->status(), "Erro en {$url}");
      }
    }

    /**
     * Test para a chamada a API para devolver partidos por competicion.
     *
     * @return void
     */
    public function testResultadosByCompeticion(){
      $competicion=Competicion::all();
      foreach($competicion as $c){
        $url="/api/v1/competicion/{$c['ID']}/resultado";
        $response = $this->call('GET', $url);
        $this->assertEquals(200, $response->status(), "Erro en {$url}");
      }
    }

    /**
     * Test para a chamada a API por Xornadas.
     *
     * @return void
     */
    public function testResultadosByXornada(){
      $competicion=Competicion::all();
      foreach($competicion as $c){
        $resultado=Resultado::where('Resultado.competicionID','=',$c['ID'])
                            ->select('Xornada')
                            ->groupby('Xornada')
                            ->get();
        foreach($resultado as $xornada){
          $url="/api/v1/competicion/{$c['ID']}/resultado/xornada{$xornada['Xornada']}";
          $response = $this->call('GET', $url);
          $this->assertEquals(200, $response->status(), "Erro en {$url}");
        }
      }
    }
}
