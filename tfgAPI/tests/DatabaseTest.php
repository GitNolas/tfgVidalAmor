<?php

use Laravel\Lumen\Testing\DatabaseMigrations;
use Laravel\Lumen\Testing\DatabaseTransactions;
use App\Federacion;
use App\Resultado;
use App\Competicion;
class DatabaseTest extends TestCase
{
    /**
     * Test para a devolucion de todos os deportes da API
     *
     * @return void
     */
    public function testBDD()
    {

      $files = glob('../BDDTests/*');
      foreach($files as $file) {
        //Apertura ficheiro a probar
        $file_json_scrapers= file_get_contents($file);
        $json_scrapers = json_decode($file_json_scrapers, true);

        //Obtencion da Response
        $id=substr($file, 13);
        $url="/api/v1/competicion/{$id}/resultado";
        $response = $this->call('GET', $url);
        $json_response=json_decode($response->getContent(), true);

        //Depuracion do JSON obtido dos SCRAPERS
        $array=array();
        for($i=0; $i<count($json_scrapers); $i++) {
          if($json_scrapers[$i]['ptsL']!="" and $json_scrapers[$i]['ptsL']!=" "){
            array_push($array,$json_scrapers[$i]);
          }
        }

        //ASSERTS
        for($i=0; $i<count($json_response); $i++) {
          $this->assertEquals($array[$i]['local'], $json_response[$i]['EquipoLocal'], "Erro en {$id}");
          $this->assertEquals($array[$i]['visitante'], $json_response[$i]['EquipoVisitante'], "Erro en {$id}");
          $this->assertEquals($array[$i]['ptsL'], $json_response[$i]['PtosLocal'], "Erro en {$id}");
          $this->assertEquals($array[$i]['ptsV'], $json_response[$i]['PtosVisitante'], "Erro en {$id}");
          $this->assertEquals($array[$i]['xornada'], $json_response[$i]['Xornada'], "Erro en {$id}");
          $this->assertEquals($array[$i]['hora'], $json_response[$i]['Hora'], "Erro en {$id}");
          $this->assertEquals($array[$i]['data'], $json_response[$i]['Data'], "Erro en {$id}");
        }
      }
      }
  }
