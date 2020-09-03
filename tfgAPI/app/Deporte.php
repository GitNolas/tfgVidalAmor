<?php
namespace App;
use Illuminate\Database\Eloquent\Model;

class Deporte extends Model {
   protected $guarded = [];
   protected $table = 'Deporte';

   public function Federacion()
    {
        return $this->hasMany('App\Federacion', 'deporteID', 'ID');
    }

}
