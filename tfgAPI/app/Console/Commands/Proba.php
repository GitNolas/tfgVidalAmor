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
class Proba extends Command
{
    /**
     * The console command name.
     *
     * @var string
     */
    protected $signature = "proba:gozalo";

    /**
     * The console command description.
     *
     * @var string
     */
    protected $description = "Comando de proba";
    /**
     * Execute the console command.
     *
     * @return mixed
     */
    public function handle()
    {

        try {
          $file_json_competiciones = file_get_contents('./competiciones.json');
          $json_competiciones = json_decode($file_json_competiciones, true);
          $output=count($json_competiciones);
          $this->info($output);
        } catch (Exception $e) {
          $message= $e->getMessage();
            $this->error("An error occurred:\n $message");
        }
    }
}
