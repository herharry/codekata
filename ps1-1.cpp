int n;
    cin>>n;
    char a[10][100];
    for(int i=0;i<n;i++)
        cin>>a[i];
        
    int j=0;
    int i;
    
    for(i=1;i<n;i++)
    {
        if(a[0][j]==a[i][j])
        {
            if(i==n-1)
            {
                i=1;
                j++;
            }
        }
        else 
            break;
    }
    
    for(i=0;i<j;i++)
        cout<<a[0][i];

    return 0;