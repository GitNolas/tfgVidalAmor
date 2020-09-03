<?php
namespace App;
use Illuminate\Database\Eloquent\Model;

class Federacion extends Model {
   protected $guarded = [];
   protected $table = 'Federacion';

   public function Deporte(){
        return $this->hasOne('App\Deporte', 'ID', 'deporteID');
    }
    public function Competicion(){
       return $this->hasMany('App\Competicion', 'federacionID', 'ID');
   }
}
