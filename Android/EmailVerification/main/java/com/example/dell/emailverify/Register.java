package com.example.dell.emailverify;

import android.app.ProgressDialog;
import android.content.Intent;
import android.net.Uri;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.internal.zzbmn;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.FirebaseApp;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.auth.UserInfo;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

import java.util.Date;
import java.util.List;

public class Register extends AppCompatActivity implements View.OnClickListener{

    EditText rName,rEmail,rPassword;
    Button rRegister;
    TextView rAlRegister;

    String Name,Email,Password;

    FirebaseAuth rAuth;
    FirebaseDatabase rDBase;
    DatabaseReference rDataBase;
    ProgressDialog rDialog;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);
        //Views of XML
        rName=(EditText)findViewById(R.id.r_FullName);
        rEmail=(EditText)findViewById(R.id.r_Email);
        rPassword=(EditText)findViewById(R.id.r_PassWord);
        rRegister=(Button)findViewById(R.id.r_SignUp);
        rAlRegister=(TextView)findViewById(R.id.r_AReg);

        //for auth
        rAuth=FirebaseAuth.getInstance();
        rDBase=FirebaseDatabase.getInstance();
        rDataBase = rDBase.getReference("Users");
        rRegister.setOnClickListener(this);
        rAlRegister.setOnClickListener(this);
        rDialog=new ProgressDialog(this);
    }

    @Override
    public void onClick(View view) {
        if(view==rRegister)
        {
            NewUser();//call new user
        }
        else if(view==rAlRegister)
        {
            startActivity(new Intent(Register.this,MainActivity.class));// goto main activity on clicking already registered
        }
    }

    private void NewUser() {
        //removing extra spaces from front and back
        Name=rName.getText().toString().trim();
        Email=rEmail.getText().toString().trim();
        Password=rPassword.getText().toString().trim();
        //checking for empty fields
        if(TextUtils.isEmpty(Name))
        {
            Toast.makeText(Register.this,"Name Field Cannot Be Blank",Toast.LENGTH_SHORT).show();
            return;
        }
        else if(TextUtils.isEmpty(Email))
        {
            Toast.makeText(Register.this,"Email Field Cannot Be Blank",Toast.LENGTH_SHORT).show();
            return;
        }
        else if(TextUtils.isEmpty(Password))
        {
            Toast.makeText(Register.this,"Password Field Cannot Be Blank",Toast.LENGTH_SHORT).show();
            return;
        }
        else if(Password.length()<6)
        {
            Toast.makeText(Register.this,"Password Must be Minimum 6 Characters",Toast.LENGTH_SHORT).show();
            return;
        }
        rDialog.setMessage(" Creating User Please Wait ......");
        rDialog.setCanceledOnTouchOutside(false);
        rDialog.show();
        rAuth.createUserWithEmailAndPassword(Email,Password).addOnCompleteListener(new OnCompleteListener<AuthResult>() {
            @Override
            public void onComplete(@NonNull Task<AuthResult> task) {
                if(task.isSuccessful())
                {
                    sendEmailVerify();// send email verification
                    rDialog.dismiss();
                    Toast.makeText(Register.this,"Account Created....",Toast.LENGTH_SHORT).show();
                    OnAuth(task.getResult().getUser());
                    FirebaseAuth.getInstance().signOut();

                }
                else
                {
                    rDialog.dismiss();
                    Toast.makeText(Register.this,"Error Creating Account",Toast.LENGTH_SHORT).show();
                }

            }
        });
    }

    private void sendEmailVerify() {
        FirebaseUser user=FirebaseAuth.getInstance().getCurrentUser();
        if(user!=null)
        {
            user.sendEmailVerification().addOnCompleteListener(new OnCompleteListener<Void>() {
                @Override
                public void onComplete(@NonNull Task<Void> task) {
                    if(task.isSuccessful())
                    {
                        Toast.makeText(Register.this,"Verification Email Sent...",Toast.LENGTH_SHORT).show();
                    }
                }
            });
        }
    }

    private void OnAuth(FirebaseUser user) {
        createNew(user.getUid());
    }

    private void createNew(String uid) {
        rDataBase.child(uid).setValue(Name);// writing name to RDBMS
    }


}
