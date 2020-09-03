<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateCompeticion extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('Competicion', function (Blueprint $table) {
            $table->increments('ID');
            $table->integer('federacionID')->unsigned();
            $table->string('Nome');
            $table->timestamps();
        });
        Schema::table('Competicion', function($table) {
		        $table->foreign('federacionID')->references('ID')->on('Federacion');
         });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('Competicion');
    }
}
