<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateFederacion extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('Federacion', function (Blueprint $table) {
            $table->increments('ID');
            $table->string('Nome');
            $table->integer('deporteID')->unsigned();
            $table->timestamps();
        });
        Schema::table('Federacion', function($table) {
		        $table->foreign('deporteID')->references('ID')->on('Deporte');
         });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('Federacion');
    }
}
