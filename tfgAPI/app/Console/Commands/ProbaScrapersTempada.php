<?php
/**
 *
 * PHP version >= 7.0
 *
 * @category Console_Command
 * @package  App\Console\Commands
 */

namespace App\Console\Commands;


use App\Resultado;

use Exception;
use Illuminate\Console\Command;



/**
 * Class deletePostsCommand
 *
 * @category Console_Command
 * @package  App\Console\Commands
 */
class ProbaScrapersTempada extends Command
{
    /**
     * The console command name.
     *
     * @var string
     */
    protected $signature = "scraper:probaTempada";

    /**
     * The console command description.
     *
     * @var string
     */
    protected $description = "Chamada a un scraper de proba para a mostra do funcionamento do sistema. So intserta os valores da primeira xornada da temporada";

    /**
     * Execute the console command.
     *
     * @return mixed
     */
    public function handle()
    {

        try {
          $output=exec("python3 ../tfgObtencionDatos/controlador.py -f -cC 9257086 -cG 9299485 -cF gal");
          $this->info("Output: $output");
          $file_json = file_get_contents($output);
          $json = json_decode($file_json, true);
          $this->info("Acceso a base de datos");
          foreach($json as $r) { //foreach element in $arr
            if($r['ptsL']!='' && $r['ptsL']!=' '){
              $resultado= Resultado::firstOrCreate(
                ['EquipoLocal' => $r['local'],
                'EquipoVisitante' => $r['visitante'],
                'PtosLocal' => $r['ptsL'],
                'PtosVisitante' => $r['ptsV'],
                'Localizacion' => $r['localizacion'],
                'Hora' => $r['hora'],
                'Data' => $r['data'],
                'xornada' => $r['xornada'],
                'competicionID' => 26]
              );
            }
          }
          $this->info("Eliminando o arquivo: $output");
          unlink($output);


        } catch (Exception $e) {
          $message= $e->getMessage();
            $this->error("An error occurred:\n $message");
        }
    }
}
