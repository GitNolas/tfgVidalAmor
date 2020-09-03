<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateResultado extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
      Schema::create('Resultado', function (Blueprint $table) {
          $table->increments('ID');
          $table->integer('competicionID')->unsigned();
          $table->string('EquipoLocal');
          $table->string('EquipoVisitante');
          $table->integer('PtosLocal');
          $table->integer('PtosVisitante');
          $table->string('Localizacion');
          $table->string('Hora');
          $table->string('Data');
          $table->integer('Xornada');
          $table->timestamps();
      });
      Schema::table('Resultado', function($table) {
          $table->foreign('competicionID')->references('ID')->on('Competicion');
       });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('Resultado');
    }
}
