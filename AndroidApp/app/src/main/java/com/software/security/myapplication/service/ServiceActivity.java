package com.software.security.myapplication.service;

import android.content.ComponentName;
import android.content.Context;
import android.content.Intent;
import android.content.ServiceConnection;
import android.os.Bundle;
import android.os.Handler;
import android.os.HandlerThread;
import android.os.IBinder;
import android.os.Looper;
import android.view.View;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.software.security.myapplication.R;

import java.text.SimpleDateFormat;
import java.util.Calendar;

public class ServiceActivity extends AppCompatActivity {

    TimeService mBoundService;
    boolean mServiceBound = false;
    TextView timestampText;
    Intent timerIntent;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_service);
        timestampText = findViewById(R.id.serviceTime);

        Calendar calendar;
        calendar = Calendar.getInstance();
        SimpleDateFormat simpleDateFormat = new SimpleDateFormat("HH:mm:ss");
        String currDateTime = simpleDateFormat.format(calendar.getTime());
        timestampText.setText(currDateTime);
    }

    @Override
    protected void onStart() {
        System.out.println("Start service");
        super.onStart();
        timerIntent = new Intent(this, TimeService.class);
        startService(timerIntent);
        bindService(timerIntent, mServiceConnection, Context.BIND_AUTO_CREATE);
    }

    public void startTimeButton(View view) throws InterruptedException {
        if(!mServiceBound){
            mServiceBound=true;
        }

        HandlerThread mHandlerThread = new HandlerThread("LocalServiceThread");
        mHandlerThread.start();
        Handler mHandler = new Handler(mHandlerThread.getLooper());
        mHandler.post(new Runnable() {
            @Override
            public void run() {
                while (mServiceBound){
                    new Handler(Looper.getMainLooper()).post(new Runnable() {
                        @Override
                        public void run() {
                            System.out.println(timestampText);
                            timestampText.setText(mBoundService.getTimestamp());
                        }
                    });
                    try {
                        Thread.sleep(1000);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }
        });
    }

    public void stopTimeButton(View view){
        mServiceBound=false;
    }

    private ServiceConnection mServiceConnection = new ServiceConnection() {
        @Override
        public void onServiceDisconnected(ComponentName name) {
            mServiceBound = false;
        }
        @Override
        public void onServiceConnected(ComponentName name, IBinder service) {
            TimeService.LocalBinder myBinder = (TimeService.LocalBinder) service;
            mBoundService = myBinder.getService();
            mServiceBound = true;
        }
    };
}