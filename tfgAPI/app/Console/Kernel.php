<?php

namespace App\Console;

use Illuminate\Console\Scheduling\Schedule;
use Laravel\Lumen\Console\Kernel as ConsoleKernel;

class Kernel extends ConsoleKernel
{
    /**
     * The Artisan commands provided by your application.
     *
     * @var array
     */
    protected $commands = [
      Commands\CallAllScrapers::class,
      Commands\Proba::class,
      Commands\ProbaScrapersXornada::class,
      Commands\ProbaScrapersTempada::class
    ];

    /**
     * Define the application's command schedule.
     *
     * @param  \Illuminate\Console\Scheduling\Schedule  $schedule
     * @return void
     */
    protected function schedule(Schedule $schedule)
    {
      $schedule->command('scrapers:all')->weekdays()->dailyAt('8:00');
      $schedule->command('scrapers:all')->weekends()->twiceDaily(13, 23);
    }
}
