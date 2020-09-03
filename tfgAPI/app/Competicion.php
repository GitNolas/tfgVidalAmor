<?php
namespace App;
use Illuminate\Database\Eloquent\Model;

class Competicion extends Model {
  protected $guarded = [];
  protected $table = 'Competicion';

  public function Federacion(){
    return $this->hasOne('App\Federacion', 'ID', 'federacionID');
  }
  public function Resultado(){
     return $this->hasMany('App\Resultado', 'competicionID', 'ID');
 }
}
