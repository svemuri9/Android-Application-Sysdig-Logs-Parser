package com.software.security.myapplication.broadcast;

import androidx.appcompat.app.AppCompatActivity;

import android.content.BroadcastReceiver;
import android.content.Intent;
import android.content.IntentFilter;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;

import com.software.security.myapplication.R;

public class BroadcastActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_broadcast);
        IntentFilter intentFilter = new IntentFilter("broadcast");
        BroadcastReceiver broadcastReceiver = new BroadcastActivityReceiver();
        registerReceiver(broadcastReceiver, intentFilter);
    }

    public void sendBroadcastButton(View view) {
        Log.d("<BROADCAST ACTIVITY: >", "Inside broadcast activity");
        EditText broadcastText = (EditText) findViewById(R.id.broadcastMessage);
        Intent intent = new Intent("broadcast");
        intent.putExtra("message", broadcastText.getText().toString());
        sendBroadcast(intent);

    }
}