# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from oslo_config import cfg
from oslo_log import log as logging

from stackanetes.k8s_instance import K8sInstance

LOG = logging.getLogger()
CONF = cfg.CONF
CONF.import_group('stackanetes', 'stackanetes.config.stackanetes')


# Public API below
##################
def run_service(service_name, service_dir):
    instance = K8sInstance(service_name, service_dir)
    instance.run()


def kill_service(service_name, service_dir):
    instance = K8sInstance(service_name, service_dir)
    instance.delete()
