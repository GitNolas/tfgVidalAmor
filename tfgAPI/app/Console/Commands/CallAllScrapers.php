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
class CallAllScrapers extends Command
{
    /**
     * The console command name.
     *
     * @var string
     */
    protected $signature = "scraper:all";

    /**
     * The console command description.
     *
     * @var string
     */
    protected $description = "Chamada a todos os scrapers do sistema de obtención de datos";

    protected function returnFilePath($c){
      if($c['deporte']=='balonman'){
        $deporte='-bm';
        $codigoCompeticion=$c['idCompeticion'];
        $path="python3 ../tfgObtencionDatos/controlador.py $deporte -cC $codigoCompeticion";
        return $path;
      }elseif($c['deporte']=='futbol'){
        $deporte='-f';
        $codigoCompeticion=$c['idCompeticion'];
        $codigoGrupo=$c['idGrupo'];
        $codigoFederacion=$c['idFederacion'];
        $path="python3 ../tfgObtencionDatos/controlador.py $deporte -cC $codigoCompeticion -cF $codigoFederacion -cG $codigoGrupo";
        return $path;
      }
    }
    /**
     * Execute the console command.
     *
     * @return mixed
     */
    public function handle()
    {

        try {
          unlink('spiderLog/pnfg.log');
          $file_json_competiciones = file_get_contents('./competiciones.json');
          $json_competiciones = json_decode($file_json_competiciones, true);
          foreach($json_competiciones as $competicion) {
            $this->info("============================================");
            $this->info("Deporte: {$competicion['deporte']}");
            $this->info("Categoria: {$competicion['nomeCategoria']}");
            $this->info("Liga: {$competicion['nomeLiga']}");
            $this->info("Federacion: {$competicion['nomeFederacion']}");
            $this->info("Spider: {$competicion['spider']}");
            $this->info("============================================");
            $filePath=$this->returnFilePath($competicion);
            $this->info("Comando: {$filePath}");
            $output=exec($filePath);
            $this->info("Output: $output");
            $file_json = file_get_contents($output);
            $json = json_decode($file_json, true);
            $this->info("Acceso a base de datos");
            foreach($json as $r) { //foreach element in $arr
              if($r['ptsL']!='' && $r['ptsL']!=' '){
                $cID=(int)$competicion['idCompeticionDB'];
                $resultado= Resultado::firstOrCreate(
                  ['EquipoLocal' => $r['local'],
                  'EquipoVisitante' => $r['visitante'],
                  'PtosLocal' => $r['ptsL'],
                  'PtosVisitante' => $r['ptsV'],
                  'Localizacion' => $r['localizacion'],
                  'Hora' => $r['hora'],
                  'Data' => $r['data'],
                  'xornada' => $r['xornada'],
                  'competicionID' => $cID]
                );
              }
            }
            $this->info("Eliminando o arquivo: $output");
            unlink($output);
          }

        } catch (Exception $e) {
          $message= $e->getMessage();
            $this->error("An error occurred:\n $message");
        }
    }
}
