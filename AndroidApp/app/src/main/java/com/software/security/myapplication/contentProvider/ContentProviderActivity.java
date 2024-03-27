package com.software.security.myapplication.contentProvider;

import androidx.appcompat.app.AppCompatActivity;

import android.content.ContentValues;
import android.database.Cursor;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.software.security.myapplication.R;

public class ContentProviderActivity extends AppCompatActivity {

    EditText inputName;
    EditText inputPhone;
    TextView contactsListView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_content_provider);

        inputName = (EditText) findViewById(R.id.nameInsert);
        inputPhone = (EditText) findViewById(R.id.phoneInsert);
        contactsListView = (TextView) findViewById(R.id.contactsShowView);
    }

    public void insertToDB(View view) {
        ContentValues values  = new ContentValues();
//        values.put(ContactDataBase.ID,new Random().nextInt(100));
        values.put(ContactDataBase.NAME,inputName.getText().toString());
        values.put(ContactDataBase.PHONE,inputPhone.getText().toString());

        getApplicationContext().getContentResolver().insert(ContactContentProvider.CONTENT_URI,values);
        Toast.makeText(this,"Inserted 1 contact ",Toast.LENGTH_SHORT).show();
        showDBEntries(view);
    }

    public void resetDB(View view) {
        int delCount =
                getContentResolver().delete(ContactContentProvider.CONTENT_URI,null,null);
        Toast.makeText(this,"Deleted " + delCount +
                " contacts",Toast.LENGTH_SHORT).show();
        showDBEntries(view);
    }

    public void showDBEntries(View view) {
        Uri uri = ContactContentProvider.CONTENT_URI;
        Cursor cursor = this.getContentResolver().query(uri,null,null,null,null);
        StringBuilder sb = new StringBuilder();
        while (cursor.moveToNext()){
            sb.append(cursor.getString(0) + ". ");
            sb.append(cursor.getString(1) + "    ");
            sb.append(cursor.getString(2) + " ");
            sb.append("\n");
        }
        contactsListView.setText(sb.toString());
    }
}