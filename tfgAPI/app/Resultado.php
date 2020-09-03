<?php
namespace App;
use Illuminate\Database\Eloquent\Model;

class Resultado extends Model {
  protected $guarded = [];
  protected $table = 'Resultado';
  public function Competicion(){
       return $this->hasOne('App\Competicion', 'ID', 'competicionID');
   }
}
