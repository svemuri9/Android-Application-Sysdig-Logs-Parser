package com.software.security.myapplication.service;

import android.app.Service;
import android.content.Intent;
import android.os.Binder;
import android.os.IBinder;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;

public class TimeService extends Service {

    private final IBinder mBinder = new LocalBinder();

    public class LocalBinder extends Binder {
        public TimeService getService() {
            return TimeService.this;
        }
    }

    public TimeService() {}

    @Override
    public IBinder onBind(Intent intent) {
        return mBinder;
    }

    public String getTimestamp() {
        String currentTime = new SimpleDateFormat("HH:mm:ss", Locale.getDefault()).format(new Date());
        return currentTime;
    }

    @Override
    public void onDestroy() {
        super.onDestroy();
    }
}