package com.software.security.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

import com.software.security.myapplication.broadcast.BroadcastActivity;
import com.software.security.myapplication.contentProvider.ContentProviderActivity;
import com.software.security.myapplication.service.ServiceActivity;

import java.text.SimpleDateFormat;
import java.util.Calendar;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        setCurrentTime();
    }

    public void launchBroadcastActivity(View view) {

        Intent in = new Intent(this, BroadcastActivity.class);
        startActivity(in);
    }

    public void launchService(View view) {

        Intent in = new Intent(this, ServiceActivity.class);
        startActivity(in);
    }

    public void launchContentProvider(View view) {

        Intent in = new Intent(this, ContentProviderActivity.class);
        startActivity(in);
    }

    private void setCurrentTime() {
        View time = findViewById(R.id.timeEditText);
        Calendar calendar;
        calendar = Calendar.getInstance();
        SimpleDateFormat simpleDateFormat = new SimpleDateFormat("HH:mm");
        String currDateTime = simpleDateFormat.format(calendar.getTime());
        ((TextView)time).setText(currDateTime);
    }


}