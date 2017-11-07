execute "apt-get update" do
  command "apt-get update"
end

package 'python3' #will install python
package 'python3-pip' #will install pip3
package 'git'

execute "export LC_ALL=C" do
  command "export LC_ALL=C"
end

execute 'pip3 install django djangorestframework pytest boto3' do
  command "pip3 install django djangorestframework pytest boto3"
end
